/*
 * Service for getting new tasks
 */
angular.module('flocs.services.task', [])
.factory('taskService', ['$http', function ($http) {

  var currentTask;

  // public API
  return {
    gettingNextTask: gettingNextTask,
    gettingAllTaskIds: gettingAllTaskIds,
    gettingTaskById: gettingTaskById,

    //reportResults: reportResults,
    getMazeSettings: getMazeSettings,
    getWorkspaceSettings: getWorkspaceSettings,
    //taskFinished: taskFinished
  };

  // private implementation

  function getMazeSettings() {
    return currentTask['maze-settings'];
  }

  function getWorkspaceSettings() {
    return currentTask['workspace-settings'];
  }

  function gettingAllTaskIds() {
    return $http.get('api/tasks/get-ids')
      .then(function(response) {
        return response.data;
      });
  }

  function gettingTaskById(id) {
    //return $http.get('api/tasks/get-task/' + id); // TODO: .then
    currentTask = {
      id: 0,
      mazeSettings: {
        grid: [
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 0, 1],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 2, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]],
        hero: {
          position: [1, 2],
          direction: 0
        }
      },
      workspaceSettings: {
        toolbox: ['maze_move_forward'],
      }
    };
    //return currentTask;
  }

  function gettingNextTask() {

    // TODO: error handling etc., separate service
    return $http.get('api/practice/next-task')
      .then(function(response) {
        currentTask = response.data;
      });


    /*currentTask = {
      id: 0,
      mazeSettings: {
        grid: [
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 2, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]],
        hero: {
          position: [1, 2],
          direction: 0
        }
      },
      workspaceSettings: {
        toolbox: null,
      }
    };
      return currentTask;*/
  }

  function reportResults() {
    // TODO
  }
}]);
