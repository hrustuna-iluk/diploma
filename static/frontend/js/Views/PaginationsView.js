var PaginationsView  = BaseView.extend({

    tagName: "ul",

    className: "pagination",

    initialize: function(options) {
        this.faculty = options.faculty;
        this.semester = options.semester;
        this.collection = new PaginationCollection();
    },

    _addPaginationElement: function() {
        if(this.semester === 1){
            for(var i = 1; i <= this.faculty.get('amountOfWeekInFirstSemester'); i++){
                new PaginationView({
                    collection: this.collection
                });
            }
        }else if(this.semester === 2){
            for(var i = 1; i <= this.faculty.get('amountOfWeekInSecondSemester'); i++){
                new PaginationView({
                    collection: this.collection
                });
            }
        }

    },

    render: function() {
        this._addPaginationElement();
        return this;
    }

});