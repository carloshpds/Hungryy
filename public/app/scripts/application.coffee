'use strict'

angular.module('hungryyApp', ['ui.router','localytics.directives'])
  .config( ($stateProvider, $urlRouterProvider) => 

    

    $stateProvider
      .state('search-food', 
        url        : '/search-food',
        templateUrl: 'views/search-food.html',
        controller : 'FoodController'
      )

      .state('team',
        url: '/development-team',
        templateUrl: 'views/team.html',
        controller : 'TeamController'
      )
  )
