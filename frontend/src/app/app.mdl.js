/**
 * Flocs application module
 */
angular.module('flocs', [
    'templates-app',
    'templates-common',
    'ui.router',
    'flocs.home',
    'flocs.practice',
    'flocs.taskPreview',
    'flocs.login'
])

// routes configuration
.config(['$httpProvider', '$stateProvider', '$locationProvider',
  function($httpProvider, $stateProvider, $locationProvider) {

  // settings for CSRF protection
  // (Django uses different name for CSFR cookie than Angular by default)
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

  /*
  // For any unmatched url, redirect to /404
  $urlRouterProvider.otherwise("/404");
  */

  // States
  $stateProvider
    .state('home', {
      url: '/',
      templateUrl: 'home/home.tpl.html',
      controller: 'homeCtrl'
    })

    .state('task-preview-unset', {
      url: '/task-preview',
      templateUrl: 'task-preview/task-preview.tpl.html',
      controller: 'taskPreviewCtrl'
    })

    .state('task-preview-set', {
      url: '/task-preview/{taskId:int}',
      templateUrl: 'task-preview/task-preview.tpl.html',
      controller: 'taskPreviewCtrl'
    })

    .state('practice', {
      url: '/practice',
      templateUrl: 'practice/practice.tpl.html',
      controller: 'practiceCtrl'
    })

    .state('login',{
      url: '/login',
      templateUrl: 'login/login.tpl.html',
      controller: 'loginCtrl'
    })

    .state('register',{
      url:'/register',
      templateUrl: 'register/register.tpl.html',
      controller: 'registerCtrl'
    })

    .state('404', {
      url: '*path',
      templateUrl: '404/404.tpl.html'
    });

  // use URLs without hashes (if the browser supports HTML5 history)
  $locationProvider.html5Mode(true);

}])

// Main application controller
.controller('appCtrl', ['$scope', function($scope) {
  // global configuration (user, language) functions go here
}]);
