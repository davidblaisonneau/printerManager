name = "Prusa i3";
ip = "192.168.1.15";
key = "097681187FB44245BA4EBBACC171038B";
info = [
			{type: 'location', value: 'Armoire - niv3'},
		];

function printerController($scope,  $http) {

	$scope.init = function($name, $ip, $key, $info){
		$scope.name = $name;
		$scope.ip = $ip;
		$scope.key = $key;
		$scope.info = $info;
	}
		 
    $scope.getStatus = function () {
        getRest($scope, $http, $scope.ip, 'connection', $scope.key);
    }
		 
    $scope.getOctoPrintVersion = function () {
        getRest($scope, $http, $scope.ip, 'version', $scope.key);
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
