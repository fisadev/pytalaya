function DashboardCtrl($scope) {
  $scope.members = [];

  //event stream client
  var source = new EventSource('/api/events/');
  source.onmessage = function(event) {
    $scope.$apply(function() {
      updated_member = JSON.parse(event.data)[0];

      var length = $scope.members.length,
          member = null,
          added = false;

      for (var i = 0; i < length; i++) {
        member = $scope.members[i];
        if (member.pk === updated_member.pk) {
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
