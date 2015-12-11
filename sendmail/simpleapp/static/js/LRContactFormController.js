app.controller('LRContactFormController', ['$scope', '$http', 'vcRecaptchaService', function($scope, $http, vcRecaptchaService) {
    this.feedback = {};
    $scope.submit = function(parameters) {
        parameters['g-recaptcha-response'] = vcRecaptchaService.getResponse();
        $http.post('api/feedback/', parameters)
        this.feedback = {};
        grecaptcha.reset();
        $scope.lrContactForm.$setUntouched()
    };
}]);