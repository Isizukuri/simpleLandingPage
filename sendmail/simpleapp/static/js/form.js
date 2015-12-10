angular.module('LRLandingPage', ['reCAPTCHA'])
    .config(function (reCAPTCHAProvider) {
        // required: please use your own key :)
        reCAPTCHAProvider.setPublicKey('---KEY---');

        // optional: gets passed into the Recaptcha.create call
        reCAPTCHAProvider.setOptions({
            theme: 'clean'
        });
    })
    .controller('AppCtrl', function ($scope, reCAPTCHA) {

        // or you can also set key here
        reCAPTCHA.setPublicKey('---KEY---');

    });