var ClassesView = BaseView.extend ({

    tagName: 'tr',

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

    initialize: function(options) {
        this.numberOfClass = options.numberOfClass;
        this.collection = options.collection;
        this.numberOfWeek = options.numberOfWeek;
        this.scheduleModel = options.scheduleModel;
        this.teacherCollection = options.teacherCollection;
    },

    _buildRow: function() {
        if(!this.collection.length) {
            this.days.forEach($.proxy(function (day, index, array) {
               var model = new ClassModel({
                   day: index + 1,
                   number: this.numberOfClass,
                   numberOfWeek: this.numberOfWeek,
                   schedule: this.scheduleModel
               });
               this.$el.append(
                   new ClassView({
                       model: model,
                       teacherCollection: this.teacherCollection
                   }).render().$el
               );
            }, this));
        }
    },

    render: function() {
        this._buildRow();
        return this;
    }
});