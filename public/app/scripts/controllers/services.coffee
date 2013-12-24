'use strict'

angular.module('hungryyApp')
  
  # ====================================================
  # Controller
  # ====================================================
  .controller 'FoodController',  ($scope, FactoryRequest) =>


    # ====================================================
    # Methods
    # ==================================================== 
    $scope.mock = [
      {value: 1, label: 'pao'}
      {value: 2, label: 'presunto'}
      {value: 3, label: 'queijo'}
      {value: 4, label: 'salsicha'}
    ]
    

    $scope.selecionadas = []
  # ====================================================
  # Factory
  # ====================================================
  .factory 'FactoryRequest', ($http) =>
    get: (site)->
      $http 
        url: 'start'
        method:'GET'
        params:
          site: site



  