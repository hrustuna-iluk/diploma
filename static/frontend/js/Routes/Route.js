var Route = Backbone.Router.extend({

    routes: {
        "": "startPage",
        "startPage": "startPage",
        'teachers/:departmentId': 'teachers',
        'groups/:departmentId' : 'groups',
        'students/:groupId' : 'students',
        'reduction/:groupId': 'reduction',
        'scheduler/:groupId': 'scheduler',
        'journal/:groupId': 'journal',
        'publicOrders/:groupId': 'publicOrders',
        'adminPage': 'adminPage',
        'search': 'searchPage',
        'search/:departmentId': 'searchPage',
        'search/:departmentId/:groupId': 'searchPage'
    },

    currentView: null,

    initialize: function() {
        this.facultyCollection = new FacultyCollection();
        this.departmentsCollection = new DepartmentsCollection();
        this.teachersCollection = new TeachersCollection();
        this.groupsCollection = new GroupsCollection();
        this.studentsCollection = new StudentsCollection();
        this.passesCollection = new PassesCollection();
        this.classesCollection = new ClassesCollection();
        this.languagesCollection = new LanguagesCollection();
        this.benefitsCollection = new BenefitsCollection();
        this.publicPlanCollection = new PublicPlanCollection();
        this.workWithStudentCollection = new WorkWithStudentCollection();
        this.facultyCollection.fetch({ async: false });
        //this._initializeEvents();

        this.on('route', function () {
            $('.modal:visible').modal('hide');
        });

    },

    _initializeEvents: function() {
        this.on('route:startPage', this.startPage);
        this.on('route:teachers:', this.teachers);
        this.on('route:groups:', this.groups);
        this.on('route:students:', this.students);
        this.on('route:reduction:', this.reduction);
        this.on('route:scheduler:', this.scheduler);
        this.on('route:journal:', this.journal);
        this.on('route:publicOrders:', this.publicOrders);
        this.on('route:adminPage:', this.adminPage);

    },

    startPage: function() {
        var facultyReady = $.Deferred();
        var facultyModel = new FacultyModel();

        $.when(
            facultyReady,
            this.departmentsCollection.fetch({data: {screen: 'departments'}, processData: true}),
            this.teachersCollection.fetch({data: {screen: 'departments'}, processData: true})
        ).done($.proxy(function () {
            var startPageView = new StartPageView({
                collection: this.departmentsCollection,
                teachersCollection: this.teachersCollection,
                faculty: facultyModel
            });
            this.routeChanged(startPageView);
        }, this));
        if(!this.facultyCollection.length) {
            facultyModel.set({ dean: null }).save({ success: facultyReady.resolve });
        } else {
            facultyModel = this.facultyCollection.models[0];
            facultyReady.resolve();
        }
    },

    teachers: function(departmentId) {
        $.when(
            this.departmentsCollection.fetch({data: {screen: 'teachers', department: departmentId}, processData: true}),
            this.teachersCollection.fetch({data: {screen: 'teachers', department: departmentId}, processData: true})
        ).done($.proxy(function () {
            var department = this.departmentsCollection.findWhere({id: +departmentId});
            var teachersView = new TeachersView({
                department: department,
                faculty: this.facultyCollection.models[0],
                collection: this.teachersCollection
            });
            this.routeChanged(teachersView);
        }, this));
    },

    students: function(groupId) {
        $.when(
            this.groupsCollection.fetch({data: {screen: 'students', group: groupId}, processData: true}),
            this.studentsCollection.fetch({data: {screen: 'students', group: groupId}, processData: true}),
            this.benefitsCollection.fetch({data: {screen: 'students', group: groupId}, processData: true}),
            this.languagesCollection.fetch({data: {screen: 'students', group: groupId}, processData: true})
        ).done($.proxy(function () {
            var group = this.groupsCollection.findWhere({id: +groupId});
            var studentsView = new StudentsView({
                group: group,
                collection: this.studentsCollection,
                benefitsCollection: this.benefitsCollection,
                languagesCollection: this.languagesCollection
            });
            this.routeChanged(studentsView);
        }, this));
    },

    groups: function(departmentId) {
         $.when(
             this.departmentsCollection.fetch({data: {screen: 'groups', department: departmentId}, processData: true}),
             this.groupsCollection.fetch({data: {screen: 'groups', department: departmentId}, processData: true}),
             this.teachersCollection.fetch({data: {screen: 'groups', department: departmentId}, processData: true})
         ).done($.proxy(function () {
            var department = this.departmentsCollection.findWhere({id: +departmentId});
            var groupsView = new GroupsView({
                department: department,
                collection: this.groupsCollection,
                teachersCollection: this.teachersCollection
            });
            this.routeChanged(groupsView);
        }, this));
    },

    reduction: function(groupId) {
        $.when(
            this.groupsCollection.fetch({data: {screen: 'reduction', group: groupId}, processData: true}),
            this.passesCollection.fetch({data: {screen: 'reduction', group: groupId}, processData: true}),
            this.classesCollection.fetch({data: {screen: 'reduction', group: groupId}, processData: true}),
            this.studentsCollection.fetch({data: {screen: 'reduction', group: groupId}, processData: true})
        ).done($.proxy(function () {
            var group = this.groupsCollection.findWhere({id: +groupId});
            var reductionView = new ReductionView({
                group: group,
                faculty: this.facultyCollection.models[0],
                passesCollection: this.passesCollection,
                studentsCollection: this.studentsCollection,
                classesCollection: this.classesCollection
            });
            this.routeChanged(reductionView);
            }, this)
        );
    },

    scheduler: function(groupId) {
        $.when(
            this.groupsCollection.fetch({data: {screen: 'scheduler', group: groupId}, processData: true}),
            this.classesCollection.fetch({data: {screen: 'scheduler', group: groupId}, processData: true}),
            this.teachersCollection.fetch({data: {screen: 'scheduler', group: groupId}, processData: true})
        ).done($.proxy(function () {
            var group = this.groupsCollection.findWhere({id: +groupId});
            var schedulerView = new ScheduleView({
                group: group,
                collection: this.classesCollection,
                teachersCollection: this.teachersCollection
            });
            this.routeChanged(schedulerView);
        }, this));
    },

    journal: function(groupId) {
        $.when(
            this.groupsCollection.fetch({data: {screen: 'journal', group: groupId}, processData: true}),
            this.studentsCollection.fetch({data: {screen: 'journal', group: groupId}, processData: true}),
            this.publicPlanCollection.fetch({data: {screen: 'journal', group: groupId}, processData: true}),
            this.workWithStudentCollection.fetch({data: {screen: 'journal', group: groupId}, processData: true})
        ).done($.proxy(function () {
            var group = this.groupsCollection.findWhere({id: +groupId});
            var teacherJournalView = new TeacherJournalView({
                group: group,
                studentsCollection: this.studentsCollection,
                publicPlanCollection: this.publicPlanCollection,
                workWithStudentCollection: this.workWithStudentCollection
            });
            this.routeChanged(teacherJournalView);
            teacherJournalView._wrapTab();
         }, this));
    },

    publicOrders: function(groupId) {
        $.when(
            this.groupsCollection.fetch({data: {screen: 'publicOrders', group: groupId}, processData: true}),
            this.studentsCollection.fetch({data: {screen: 'publicOrders', group: groupId}, processData: true})
        ).done($.proxy(function () {
            var group = this.groupsCollection.findWhere({id: +groupId});
            var publicOrdersView = new AddPublicOrdersOfGroupView({
                group: group,
                studentsCollection: this.studentsCollection
            });
            this.routeChanged(publicOrdersView);
            publicOrdersView.renderForm();
            publicOrdersView.renderTable();
        }, this));
    },

    searchPage: function (departmentId, groupId) {
        $.when(
            this.passesCollection.fetch({data: {screen: 'search'}, processData: true}),
            this.studentsCollection.fetch({data: {screen: 'search'}, processData: true}),
            this.classesCollection.fetch({data: {screen: 'search'}, processData: true})
        ).done($.proxy(function () {
            var searchView = new SearchView({
                departmentId: departmentId,
                classesCollection: this.classesCollection,
                passesCollection: this.passesCollection,
                studentsCollection: departmentId ?
                    this.studentsCollection.filter(function (student) {
                        if (groupId) {
                            return student.get('group').id == groupId;
                        }
                        return student.get('group').department.id === +departmentId;
                    }) : this.studentsCollection
            });
            this.routeChanged(searchView);
        }, this));
    },

    adminPage: function() {
        $.when(
            this.teachersCollection.fetch({data: {screen: 'admin'}, processData: true}),
            this.studentsCollection.fetch({data: {screen: 'admin'}, processData: true}),
            this.groupsCollection.fetch({data: {screen: 'admin'}, processData: true})
        ).done($.proxy(function () {
            var adminView = new AdminPageView({
                faculty: this.facultyCollection.models[0],
                teachersCollection: this.teachersCollection,
                studentsCollection: this.studentsCollection,
                groupsCollection: this.groupsCollection
            });
            this.routeChanged(adminView);
            adminView._addFacultyInformation();
        }, this));

    },

    routeChanged: function(view) {
        if (this.currentView) {
            this.currentView.remove();
        }
        $('#main').html( view.render().el );
        this.currentView = view;
    },

    route: function(route, name, callback) {
        var router = this;
        if (!callback) callback = this[name];

        var f = function(params) {
            var args = arguments;
            this.trigger('routeBefore', route);
            callback.apply(router, args);
            this.trigger('routeAfter', route);
        };
        return Backbone.Router.prototype.route.call(this, route, name, f);
    }
});

$(document).bind("ajaxSend", function(){
    $(".loading-container").show();
}).bind("ajaxComplete", function(evt, resp){
    if ($.active === 1) {
        $(".loading-container").hide();
        if (resp.status === 403) {
            alert('Доступ заборонено');
            window.history.back();
        }
    }
});


var route = new Route;
Backbone.history.start();