'use strict'

angular.module('hungryyApp')
  
  # ====================================================
  # Controller
  # ====================================================
  .controller 'FoodController',  ($scope, resolveIngredients, FoodFactory) =>


    # ====================================================
    # Attributes
    # ==================================================== 
    $scope.ingredients         = resolveIngredients.data
    $scope.selectedIngredients = []
    $scope.resultFoods         = []

    $scope.searchFoodByIngredients = =>
      FoodFactory.searchFoodByIngredients($scope.selectedIngredients)
        .success (data, status, headers, config) =>
          if data is 'null' or data is null
            $scope.resultFoods = []
          else
            $scope.resultFoods = data

        .error (data, status, headers, config) =>
          alert 'ERROR: ' + data + ' Status Code: ' + status



