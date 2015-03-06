function printerController($scope,  $http) {

    $scope.getStatus = function () {
		$scope.printer = printers[$scope.printer];
		console.log($scope.printer);
        //~ getRest($scope, $http, $scope.printer.ip, 'connection', $scope.printer.key);
    }
		 
    $scope.getOctoPrintVersion = function () {
        //~ getRest($scope, $http, $scope.ip, 'version', $scope.key);
    }
}

//~ printerController.prototype.getStatus = function() {
  //~ this.status = getRest(this.http,"connection", $this.key);
//~ };

function getRest($scope, $http, $ip, $api, $key) {
    $http.get("http://"+$ip+"/api/"+$api+"?apikey="+$key).
        success(function(data) {
			$scope.data = data;
        });
}
//~ 
//~ function Rest($scope, $http) {
    //~ $http.get('http://192.168.1.15/api/connection?apikey=097681187FB44245BA4EBBACC171038B').
        //~ success(function(data) {
            //~ $scope.rest = data;
        //~ });
//~ }
