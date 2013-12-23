'use strict'

angular.module('apiExplorerApp')
  .controller 'TeamController', ($scope) ->
    $scope.teamGroup = [
      { 
        name    : 'Carlos Henrique'
        job     : 'Developer at DClick Web & Mobile Solutions (trainee)'
        github  : 'https://github.com/carloshpds' 
        linkedin: 'http://www.linkedin.com/profile/view?id=143700778&trk=nav_responsive_tab_profile_pic'
        img     : 'http://en.gravatar.com/userimage/48673773/404bc9a97d6861c0e70b17e7624ebc83.jpg?size=200'
      }
    ]
