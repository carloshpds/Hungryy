'use strict'

angular.module('hungryyApp')
  .factory 'FoodFactory', ($http) ->

    baseURL = 'api/food/'
    
    searchFoodByIngredients: (ingredientsIds) =>
      $http 
        url    : baseURL + 'searchFoodByIngredients'
        method :'GET'
        params :
          ingredientsIds: ingredientsIds
