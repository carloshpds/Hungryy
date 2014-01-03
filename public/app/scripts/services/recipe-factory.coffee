'use strict'

angular.module('hungryyApp')
  .factory 'RecipeFactory', ($http) ->

    baseURL = 'api/recipe/'
    
    searchRecipeByIngredients: (ingredientsIds) =>
      $http 
        url    : baseURL + 'searchRecipeByIngredients'
        method :'GET'
        params :
          ingredientsIds: ingredientsIds
