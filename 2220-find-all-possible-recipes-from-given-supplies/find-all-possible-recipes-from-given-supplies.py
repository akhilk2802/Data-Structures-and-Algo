class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
        yeast -> bread
        flour -> bread

        yeast -> bread
        flour -> bread
        '''
        graph = defaultdict(list)
        indegree = defaultdict(int)

        recipe_set = set(recipes)
        all_items = set(supplies)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                indegree[recipe] += 1

        queue = deque(supplies)
        result = []

        while queue:
            item = queue.popleft()

            for recipe in graph[item]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)

        return result

