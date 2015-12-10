app.controller('LRContactFormController', function($scope, $http, reCAPTCHA) {
	this.feedback = {};
	$scope.submit = function(parameters){
		$http.post('api/feedback/', parameters)
		this.feedback = {};
		$scope.lrContactForm.$setUntouched()
	};
});