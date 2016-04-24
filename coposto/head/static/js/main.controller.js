(function () {
  'use strict';

  angular
  .module('coposto')
  .controller('MainController', MainController);

  MainController.$inject = ['$q', '$scope', 'util'];

  /* @ngInject */
  function MainController($q, $scope, util) {
    var vm = this;

    vm.loading = true;
    vm.submitting = false;
    vm.stuff = null;

    vm.isDisabled = isDisabled;
    vm.submit = submit;

    activate();

    function activate() {
      load().then(function () {
        vm.loading = false;
      });
    }

    function load() {
      return $q.all(['Send']).then(function (results) {
        vm.send = results[0];
      });
    }

    function isDisabled() {
      return !(vm.stuff && vm.stuff.length > 0);
    }

    function submit() {
      vm.submitting = true;
      console.log(vm.stuff);
      util.toast('Submitted', vm.stuff);
      vm.submitting = false;
    }
  }
})();
