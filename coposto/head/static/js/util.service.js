(function() {
  'use strict';

  angular
  .module('coposto', ['toaster', 'ngAnimate'])
  .service('util', util);

  util.$inject = ['$http', '$q', 'toaster'];

  /* @ngInject */
  function util($http, $q, toaster) {
    var service = {
      toast: toast,

      // HTTP
      get: get,
      post: post
    };

    return service;

    // ----------

    function toast(title, text, type) {
      if (typeof(type)==='undefined') type='error';
      if (typeof(title)==='undefined') title='';
      toaster.pop({
          type: type,
          title: title,
          body: text,
          timeout: 3000
      });
    }

    function get(url, params) {
      return $http.get(url, {params: params || {}}).then(function (response) {
        return response.data;
      }, function (response) {
        return $q.reject(response.status);
      });
    }

    function post(url, data, options) {
      return $http.post(url, data, options).then(function (response) {
        return response.data;
      }, function (response) {
        return $q.reject(response.status);
      });
    }
  }
}());

