function DashboardCtrl($scope) {
  $scope.members = [];

  //event stream client
  var source = new EventSource('/api/events/');
  source.onmessage = function(event) {
    $scope.$apply(function() {
      data = JSON.parse(event.data);
      $scope.members = data;
    });
  };
}

$(document).ready(function() {
});
