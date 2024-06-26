/*jshint esversion: 6 */
/* globals $, Stripe */

window.addEventListener('DOMContentLoaded', () => {
    /*
        Core logic/payment flow for this comes from here:
        https://stripe.com/docs/payments/accept-a-payment

        CSS from here: 
        https://stripe.com/docs/stripe-js
    */

    // Extracting Stripe public key and client secret from the HTML page's django tags
    const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    const clientSecret = $('#id_client_secret').text().slice(1, -1);

    // Initializing Stripe.js with the public key
    const stripe = Stripe(stripePublicKey);

    // Creating an instance of Stripe elements
    const elements = stripe.elements();

    // Custom styling for the card element
    const style = {
        base: {
            color: '#041384',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    // Creating a card element with custom style
    const card = elements.create('card', {style: style});

    // Mounting the card element to the DOM
    card.mount('#card-element');

    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    const checkBox = document.getElementById('myCheckbox');

    checkBox.addEventListener('change', function() {
    if (this.checked) {
        console.log('checked');
        card.update({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
    } else {
        console.log('unchecked');
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
    }
    });



    // Handling real-time validation errors on the card element
    card.addEventListener('change', function (event) {
        let errorDiv = document.getElementById('card-errors');
        if (event.error) {
            let html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handling form submission
    const form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        
        // Preventing default form submission behavior
        ev.preventDefault();

        // Disabling card element and submit button, and showing loading overlay
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);

        // Extracting data from the form and preparing for submission
        let saveInfo = Boolean($('#id-save-info').attr('checked'));
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        let postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        let url = '/checkout/cache_checkout_data/';

        // Sending data to the server for caching
        $.post(url, postData).done(function () {
            // Confirming card payment with Stripe
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.name.value),
                        phone: $.trim(form.phone.value),
                        email: $.trim(form.email.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.name.value),
                    phone: $.trim(form.phone.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    // Displaying error message and reverting UI changes
                    let errorDiv = document.getElementById('card-errors');
                    let html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                    card.update({ 'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        // Submitting the form if payment is successful
                        form.submit();
                    }
                }
            });
        }).fail(function () {
            // Reloading the page if there's an error
            location.reload();
        });
    });

});
