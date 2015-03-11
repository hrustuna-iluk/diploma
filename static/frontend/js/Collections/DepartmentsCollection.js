var DepartmentsCollection = Backbone.Collection.extend ({

    url: '/departments',
    model: DepartmentModel
});