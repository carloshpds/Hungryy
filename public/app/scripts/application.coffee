'use strict'

angular.module('hungryyApp', ['ui.router','localytics.directives'])
  .config( ($stateProvider, $urlRouterProvider) => 

    $urlRouterProvider.otherwise('/search-food')
    
    $stateProvider
      .state('search-food', 
        url        : '/search-food',
        templateUrl: 'views/search-food.html',
        controller : 'FoodController'
        resolve    : 
          resolveIngredients: ($q,$timeout,IngredientFactory) =>
            return IngredientFactory.listIngredients()
      )

      .state('team',
        url: '/development-team',
        templateUrl: 'views/team.html',
        controller : 'TeamController'
      )
  )
