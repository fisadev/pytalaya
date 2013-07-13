function DashboardCtrl($scope) {
  $scope.members = [];

  //event stream client
  var source = new EventSource('/api/event_stream/');
  source.onmessage = function(event) {
    $scope.$apply(function() {
      data = JSON.parse(event.data);
      $scope.members = data;
    });
  };
}

$(document).ready(function() {
});
