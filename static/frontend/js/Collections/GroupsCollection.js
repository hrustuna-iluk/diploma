var GroupsCollection = Backbone.Collection.extend ({

    url: '/api/groups',

    model: GroupModel

});