function DashboardCtrl($scope) {
  $scope.members = [];

  //event stream client
  var source = new EventSource('/api/events/');
  source.onmessage = function(event) {
    $scope.$apply(function() {
      updated_member = JSON.parse(event.data);

      var length = $source.members.length,
          member = null,
          added = false;

      for (var i = 0; i < length; i++) {
        member = $scope.members[i];
        if (member.id === updated_member.id) {
          $scope.members[i] = updated_member;
          added = true;
          i = length;
        }
      }

      if (!added) {
        $scope.members.push(updated_member);
      }
    });
  };
}

$(document).ready(function() {
});
