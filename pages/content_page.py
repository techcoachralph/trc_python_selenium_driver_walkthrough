class ContentPage:
    def home(self):
        from pages.home import HomePage
        return HomePage

    def search_results(self):
        from pages.search_results import SearchResults
        return SearchResults

    def restaurant_details(self):
        from pages.restaurant import RestaurantDetails
        return RestaurantDetails

    def item_details(self):
        from pages.item_details import ItemDetails
        return ItemDetails

    def navigation(self):
        from pages.navigation import NavigationMenu
        return NavigationMenu

