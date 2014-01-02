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
      selected = []
      for item in $scope.selectedIngredients
        selected.push parseInt(item)

      FoodFactory.searchFoodByIngredients(selected)
        .success (data, status, headers, config) =>
          if data is 'null' or data is null
            $scope.resultFoods = []
          else
            $scope.resultFoods = data

        .error (data, status, headers, config) =>
          alert 'ERROR: ' + data + ' Status Code: ' + status

    $scope.mouseenterFoodItemHandler = ($event) =>
      $target   = $ $event.currentTarget
      $foodItem = $target.find '.item-result-food-container'
      
      $foodItem.animate
        height : ( $target.height() + 40 ) + 'px'
        width  : ( $target.width()  + 40 ) + 'px'
        , 'fast' 
      return

    $scope.mouseleaveFoodItemHandler = ($event) =>
      $target   = $ $event.currentTarget
      $foodItem = $target.find '.item-result-food-container'
      
      $foodItem.animate
        height : ( $target.height() - 40 ) + 'px'
        width  : ( $target.width()  - 40 ) + 'px'
        , 'fast'
      return

 