# Clases base (Recipe, Node, RecipeBookBase)

class RecipeBook(RecipeBookBase):
    total_recipes_created = 0

    def add_recipe(self, recipe):
        super().add_recipe(recipe) # Llama al método original
        RecipeBook.total_recipes_created += 1

    def remove_recipe(self, index):
        # Lógica de eliminación (similar a los anteriores)
        # ...
        return self.remove_item_at_index(index) # Suponiendo método auxiliar
    
    @property
    def average_cooking_time(self):
        if self.get_size() == 0:
            return 0
        total_time = 0
        curr = self.first
        while curr:
            total_time += curr.value.cooking_time_min
            curr = curr.next
        return total_time / self.get_size()

    def find_recipes_for_servings(self, num_servings):
        found_recipes = []
        curr = self.first
        while curr:
            if curr.value.servings == num_servings:
                found_recipes.append(curr.value)
            curr = curr.next
        return found_recipes