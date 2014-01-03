'use strict'

angular.module('hungryyApp')
  
  # ====================================================
  # Controller
  # ====================================================
  .controller 'RecipeController',  ($scope, resolveIngredients, RecipeFactory) =>


    # ====================================================
    # Attributes
    # ==================================================== 
    $scope.ingredients         = resolveIngredients.data
    $scope.selectedIngredients = []
    $scope.resultFoods         = []

    $scope.searchRecipeByIngredients = =>
      selected = []
      for item in $scope.selectedIngredients
        selected.push parseInt(item)

      if selected.length
        RecipeFactory.searchRecipeByIngredients(selected)
          .success (data, status, headers, config) =>
            if data is 'null' or data is null
              $scope.resultFoods = []
            else
              $scope.resultFoods = data

          .error (data, status, headers, config) =>
            alert 'ERROR: ' + data + ' Status Code: ' + status

    $scope.mouseenterRecipeItemHandler = ($event) =>
      $target   = $ $event.currentTarget
      $foodItem = $target.find '.item-result-food-container'
      
      $foodItem.stop( true, true ).animate
        height : ( $target.height() + 5 ) + 'px'
        width  : ( $target.width()  + 5 ) + 'px'
        , 'fast' 
      return

    $scope.mouseleaveRecipeItemHandler = ($event) =>
      $target   = $ $event.currentTarget
      $foodItem = $target.find '.item-result-food-container'
      
      $foodItem.stop( true, true ).animate
        height : ( $target.height() - 5 ) + 'px'
        width  : ( $target.width()  - 5 ) + 'px'
        , 'fast'
      return

 