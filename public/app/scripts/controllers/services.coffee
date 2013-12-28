'use strict'

angular.module('hungryyApp')
  
  # ====================================================
  # Controller
  # ====================================================
  .controller 'FoodController',  ($scope, resolveIngredients) =>


    # ====================================================
    # Attributes
    # ==================================================== 
    $scope.ingredients         = resolveIngredients.data
    $scope.selectedIngredients = []


  