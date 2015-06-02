var StudentFiltersView  = BaseView.extend({

    template: _.template($("#studentPassInfo").html()),

    optionBenefitTemplate: _.template($("#optionStudentPassClassTemplate").html()),

    initialize: function(options) {
        this.passesCollection = options.passesCollection;
        this.classesCollection  = options.classesCollection;
        this.studentId = options.studentId;
    },

    _attachEvents: function() {
        this.$('.closeModal').on("click", $.proxy(this._closeModal,this));
        this.$('#filterButton').on("click", $.proxy(this._filterPasses,this));
    },

    _filterPasses: function(evt) {
        evt.preventDefault();
        var passes = 0;
        if(this.$('#filterByDate').is(':checked')) {

        }else if(this.$('#filterByClass').is(':checked')) {
            this.passesCollection.each(function(model) {
                if(model.get('class_passed').subject === this.$('#studentPassClass').val() &&
                    this.studentId === model.get('student').id) {
                    passes++;
                } else {
                   return;
                }

            }, this);
            this.$('.modal-body').append("<div>"+"Кількість пропусків - "+ passes + " з дисципліни " + "'" + this.$('#studentPassClass').val()+ "'" +"</div>")
        }
    },

    _closeModal: function() {
        this.remove();
        $('body').removeClass('modal-open');
        $('.modal-backdrop').hide();
    },

    _fillClassesList: function() {
        var classes = [];
        this.classesCollection.each(function(model) {
            if(classes.indexOf(model.getSubject()) > -1) return;
            classes.push(model.getSubject());
            this.$('#studentPassClass').append(this.optionBenefitTemplate(model.toJSON()));
        }, this);
    },

    render: function() {
        this.$el = $(this.template());
        this._attachEvents();
        this._fillClassesList();
        this.$el.modal('show');
        return this;
    }

});