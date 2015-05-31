var DepartmentsCollection = Backbone.Collection.extend ({

    url: '/api/departments',

    model: DepartmentModel

});