var Route = Backbone.Router.extend({

    routes: {
        "": "startPage",
        'teachers/:departmentId': 'teachers',
        'groups/:departmentId' : 'groups',
        'students/:groupId' : 'students',
        'reduction/:groupId': 'reduction',
        'scheduler/:groupId': 'scheduler',
        'journal/:groupId': 'journal',
        'publicOrders/:groupId': 'publicOrders',
        'adminPage': 'adminPage'
    },

    currentView: null,

    initialize: function() {
        this.departmentsCollection = new DepartmentsCollection();
        this.teachersCollection = new TeachersCollection();
        this.groupsCollection = new GroupsCollection();
        this.studentsCollection = new StudentsCollection();
        this.passesCollection = new PassesCollection();
        this.classesCollection = new ClassesCollection();
        this.languagesCollection = new LanguagesCollection();
        this.benefitsCollection = new BenefitsCollection();
        this.attendanceCollection = new AttendanceCollection();
        this.publicPlanCollection = new PublicPlanCollection();
        this.workWithStudentCollection = new WorkWithStudentCollection();
        this.facultyCollection = new FacultyCollection();
        this.departmentsCollection.fetch();
        this._initializeEvents();

    },

    _initializeEvents: function() {
        this.on('route:startPage', this.startPage);
        this.on('route:teachers:', this.teachers);
        this.on('route:groups:', this.teachers);
        this.on('route:students:', this.students);
        this.on('route:reduction:', this.reduction);
        this.on('route:scheduler:', this.scheduler);
        this.on('route:journal:', this.journal);
        this.on('route:publicOrders:', this.publicOrders);
        this.on('route:adminPage:', this.adminPage);

    },

    startPage: function() {
        this.facultyCollection.fetch({
            success: $.proxy(function () {
                if(!this.facultyCollection.length) {
                    var facultyModel = new FacultyModel();
                } else {
                    var facultyModel = this.facultyCollection.models[0];
                }
                var startPageView = new StartPageView({
                    collection: this.departmentsCollection,
                    teachersCollection: this.teachersCollection,
                    faculty: facultyModel
                });
                this.routeChanged(startPageView);
            }, this)
        });
    },

    teachers: function(departmentId) {
        this.departmentsCollection.fetch({
            success: $.proxy(function () {
                var department = this.departmentsCollection.findWhere({id: +departmentId});
                var teachersView = new TeachersView({
                    department: department,
                    collection: this.teachersCollection
                });
                this.routeChanged(teachersView);
            }, this)
        });
    },

    students: function(groupId) {
        this.groupsCollection.fetch({
            success: $.proxy(function () {
                var group = this.groupsCollection.findWhere({id: +groupId});
                var studentsView = new StudentsView({
                    group: group,
                    collection: this.studentsCollection,
                    benefitsCollection: this.benefitsCollection,
                    languagesCollection: this.languagesCollection
                });
                this.routeChanged(studentsView);
            }, this)
        });
    },

    groups: function(departmentId) {
         this.departmentsCollection.fetch({
            success: $.proxy(function () {
                var department = this.departmentsCollection.findWhere({id: +departmentId});
                var groupsView = new GroupsView({
                    department: department,
                    collection: this.groupsCollection,
                    teachersCollection: this.teachersCollection
                });
                this.routeChanged(groupsView);
            }, this)
        });
    },

    reduction: function(groupId) {
        this.groupsCollection.fetch({
            success: $.proxy(function () {
                var group = this.groupsCollection.findWhere({id: +groupId});
                var reduction = this.attendanceCollection.find({group: +groupId});
                if(!reduction) {
                    reduction = new AttendanceModel({
                        group: group
                    })
                }
                var reductionView = new ReductionView({
                    model: reduction,
                    group: group,
                    collection: this.passesCollection
                });
                this.routeChanged(reductionView);
            }, this)
        });
    },

    scheduler: function(groupId) {
        this.groupsCollection.fetch({
            success: $.proxy(function () {
                var group = this.groupsCollection.findWhere({id: +groupId});
                var schedulerView = new ScheduleView({
                    group: group,
                    collection: this.classesCollection,
                    teachersCollection: this.teachersCollection
                });
                this.routeChanged(schedulerView);
            }, this)
        });
    },

    journal: function(groupId) {
        this.groupsCollection.fetch({
            success: $.proxy(function () {
                var group = this.groupsCollection.findWhere({id: +groupId});
                var teacherJournalView = new TeacherJournalView({
                    group: group,
                    studentsCollection: this.studentsCollection,
                    publicPlanCollection: this.publicPlanCollection,
                    workWithStudentCollection: this.workWithStudentCollection
                });
                this.routeChanged(teacherJournalView);
                teacherJournalView._wrapTab();
             }, this)
        });
    },

    publicOrders: function(groupId) {
        this.groupsCollection.fetch({
            success: $.proxy(function () {
                var group = this.groupsCollection.findWhere({id: +groupId});
                var publicOrdersView = new AddPublicOrdersOfGroupView({
                    group: group,
                    studentsCollection: this.studentsCollection
                });
                this.routeChanged(publicOrdersView);
                publicOrdersView.renderForm();
                publicOrdersView.renderTable();
            }, this)
        });
    },

    adminPage: function() {},

    routeChanged: function(view) {
        if (this.currentView) {
            this.currentView.remove();
        }
        $('#main').html( view.render().el );
        this.currentView = view;
    }
});

var route = new Route;
Backbone.history.start();