'use strict'

angular.module('hungryyApp')
  .factory 'FoodFactory', ($http) ->

    baseURL = 'api/food/'
    
    searchFoodByIngredients: (ingredients) =>
      $http 
        url    : baseURL + 'searchFoodByIngredients'
        method :'GET'
        params :
          ingredients: ingredients
