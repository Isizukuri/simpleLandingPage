angular.module('LRLandingPage', ['reCAPTCHA'])
    .config(function (reCAPTCHAProvider) {
        // required: please use your own key :)
        reCAPTCHAProvider.setPublicKey('6LeSyhITAAAAAO0NUAXOGJhFCl0F9l1oHXE8CmNk');

        // optional: gets passed into the Recaptcha.create call
        reCAPTCHAProvider.setOptions({
            theme: 'clean'
        });
    })
    .controller('LRContactFormController', function ($scope, reCAPTCHA) {



    });