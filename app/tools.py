""" Module to handle various functionality that our application may need """


from .models import User, BucketList, BucketlistItems


class Storage():
    """Class will handle volatile storage of the application's data"""

    users = [{'email': None, 'password': None, 'username': None, 'id': 0}]
    bucketlists = [{'title': None, 'description': None, 'id': 0}]

    def add_user(self, username, email, password):
        """Method to register users to the application"""

        new_user = User(username, email, password)
        new_user_details = new_user.get_details()
        for user in self.users:
            if new_user_details['email'] == user['email']:
                break
                return False
            else:
                new_user_details['id'] = len(self.users)
                self.users.append(new_user_details)

    def add_bucketlist(self, title, description):
        """Method to add new bucketliists to the application"""
        new_bucketlist = BucketList(title, description)
        new_bucketlist_details = new_bucketlist.get_details()
        new_bucketlist_details['id'] = len(self.bucketlists)
        for bucketlist in self.bucketlists:
            if new_bucketlist_details['id'] == bucketlist['id']:
                new_bucketlist_details['id'] = new_bucketlist_details['id'] + 1
        self.bucketlists.append(new_bucketlist_details)

    def get_bucketlists(self):
        """Method to return all created bucketlists"""
        return self.bucketlists

    def get_single_bucketlist(self, id):
        """Method to return a single bucketlist base on a given id"""
        for bucketlist in self.bucketlists:
            if bucketlist['id'] == id:
                return bucketlist

    def remove_bucketlist(self, id):
        """Method to delete bucketlists based on the id"""
        for bucketlist in self.bucketlists:
            if bucketlist['id'] == int(id):
                self.bucketlists.remove(bucketlist)

    def add_bucketlist_item(self, bucketist_id, item, duedate):
        """
            Method to add bucketlist items to a bucketlist given the id of the
            bucketlist
        """
        new_bucketlist_item = BucketlistItems(item, duedate)
        new_item_details = new_bucketlist_item.get_details()
        bucketlist = self.get_single_bucketlist(bucketist_id)
        new_item_details['id'] = len(bucketlist['items']) + 1
        for item in bucketlist['items']:
            if new_item_details['id'] == item['id']:
                new_item_details['id'] = new_item_details['id'] + 1
        bucketlist['items'].append(new_item_details)

    def get_bucketlist_item(self, bucketlist_id, item_id):
        """
            Method to return a single bucketlist item based on the bucketlist 
            item's id and its bucketlist's id
        """
        single_bucketlist = self.get_single_bucketlist(bucketlist_id)
        for item in single_bucketlist['items']:
            if item['id'] == item_id:
                return item

    def finish_bucketlist_item(self, bucketlist_id, item_id):
        """Method used to set a bucketlist item finished attribute to true"""
        single_bucketlist_item = self.get_bucketlist_item(
            bucketlist_id,
            item_id

        )
        if single_bucketlist_item['finished']:
            single_bucketlist_item['finshed'] = False
        elif not single_bucketlist_item['finished']:
            single_bucketlist_item['finished'] = True

    def remove_bucketlist_item(self, bucketlist_id, item_id):
        """
            Method to delete a bucketlist item based on its id and its
            bucketlist's id
        """
        single_bucketlist = self.get_single_bucketlist(bucketlist_id)
        for item in single_bucketlist['items']:
            if item['id'] == int(item_id):
                single_bucketlist['items'].remove(item)


store = Storage()
