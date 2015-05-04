var ClassesView = BaseView.extend ({

    tagName: 'tr',

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

    initialize: function(options) {
        this.numberOfClass = options.numberOfClass;
        this.group = options.group;
        this.collection = options.collection;
        this.numberOfWeek = options.numberOfWeek;
        this.scheduleModel = options.scheduleModel;
        this.teachersCollection = options.teachersCollection;
        this.parentView = options.parentView;
    },

    _buildRow: function() {
        var classes = [];
            this.days.forEach($.proxy(function (weekDay, index, array) {
               var model = new ClassModel({
                   group: this.group.get('id'),
                   day: weekDay,
                   number: this.numberOfClass,
                   numberOfWeek: this.numberOfWeek,
                   schedule: this.scheduleModel
               });
               var classView = new ClassView({
                   group: this.group,
                   model: model,
                   classesCollection: this.collection,
                   teachersCollection: this.teachersCollection
               }).render();
               this.$el.append(classView.$el);
               classes.push(classView);
            }, this));
            this.parentView.classes.push(classes);
    },

    render: function() {
        this._buildRow();
        return this;
    }
});