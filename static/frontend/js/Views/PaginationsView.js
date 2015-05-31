var PaginationsView  = BaseView.extend({

    tagName: "ul",

    className: 'pagination',

    className: "pagination",

    initialize: function(options) {
        this.container = options.container;
        this.faculty = options.faculty;
        this.semester = options.semester;
        this.collection = new PaginationCollection();
        this._publisherEvents();
    },

    _publisherEvents: function () {
        this.publisher.on('passes:paginator:show:page', $.proxy(function (page) {
            this.$el.find('li:first').trigger('click');
        }, this));
    },

    _addPaginationElement: function() {
        var amountOfWeeks = null;

        if(this.semester === 1){
            amountOfWeeks = this.faculty.get('amountOfWeekInFirstSemester');
        }else if(this.semester === 2){
            amountOfWeeks = this.faculty.get('amountOfWeekInSecondSemester');
        }
        this.clear();
        for(var i = 1; i <= amountOfWeeks; i++) {
            this.$el.append(
                new PaginationView({
                    semester: this.semester,
                    faculty: this.faculty,
                    collection: this.collection
                }).render().el
            )
        }
    },

    clear: function () {
      this.collection.reset();
      this.$el.empty();
    },

    render: function() {
        this._addPaginationElement();
        this.container.empty().html( this.$el );
        return this;
    }

});