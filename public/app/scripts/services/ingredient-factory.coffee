'use strict'

angular.module('hungryyApp')
  .factory 'IngredientFactory', ($http) ->
    
    baseURL = 'api/ingredient/'

    listIngredients: =>
      $http 
        url: baseURL + 'list'
        method:'GET'