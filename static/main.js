(function () {
	var app = angular.module('app', []);
	app.controller('MainCtrl', ['$scope', '$http', '$sce', '$location', '$timeout', function ($scope, $http, $sce, $location, $timeout) {
		window.sc = $scope;
		var location = $location.absUrl();
		location = location.substring(location.length-1) == '/' ? location.substring(0, location.length - 1) : location;

		// Load tree
		$scope.is_loading = true;
		$http.get(location + '/data/tree.json').success(function (data) {
			$scope.is_loading = false;
			$scope.tree = data;
			// Load anagrams
			$http.get(location + '/data/anagrams.json').success(function (data) {
				$scope.anagrams = data;
			});
		});

		$scope.toggleSubtree = function (subtree) {
			subtree.open = !subtree.open;

			// Recursively open subtrees if they
			// only have one child
			var n_children = 0;
			for (var let in subtree) {
				if (let !== 'open') {
					var subsubtree = subtree[let];
					key = let;
					n_children += 1;
				}
				if (n_children > 1) {
					return;
				}
			}
			if (n_children === 1) {
				$scope.toggleSubtree(subsubtree);
			}
		};

		$scope.renderHtml = function(html_code) {
		    return $sce.trustAsHtml(html_code);
		};

		$scope.onType = function (event) {
			if (event.keyCode == 13) {
				$scope.selectWord($scope.searchText);
			}
		}

		$scope.selectWord = function (word) {
			$scope.selected_word = word;
			$scope.getAnagrams(word);
			$scope.getWiki(word);
		}

		$scope.getAnagrams = function (word) {
			$scope.word_anagrams = $scope.anagrams[word.split('').sort().join('')];
		};

		$scope.getWiki = function (word) {
			var conf = {
				params: {
					page: word,
					action: 'parse',
					format: 'json',
					callback: 'JSON_CALLBACK'
				}
			};

			$scope.is_loading = true;

			$http.jsonp('http://en.wikipedia.org/w/api.php', conf).success(function (data) {
				$scope.error = false;
				$scope.is_loading = false;
				$scope.info = data;
				$scope.title = data.parse && data.parse.title;
				$scope.error = $scope.info.error;

				// scroll to top
			    $timeout(function () {
				    window.document.querySelector('.wiki').scrollTop = 0;
			    });
			}).error(function (data) {
				$scope.is_loading = false;
				$scope.error = true;
			});
		};

		$scope.search = function () {
			var current = $scope.tree;
			for (var i = 0; i < $scope.searchText.length; i ++) {
				var path = $scope.searchText[i];
				if (!current[path]) {
					return;
				}
				current[path].open = true;
				current = current[path];
			}
		};

		$scope.mostAnagrams = function () {
			var biggest = 0;
			for (var key in $scope.anagrams) {
				var anagrams = $scope.anagrams[key];
				if (anagrams.length > biggest) {
					biggest = anagrams.length;
					console.log(key);
					most_anagrams = key;
				}
			}
			return most_anagrams;
		}
	}]);
})();

