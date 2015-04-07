var StartPageView = BaseView.extend ({

    tagName: "div",

    template: _.template($("#startPageTemplate").html()),

    optionHeadOfDepartmentTemplate: _.template($("#optionHeadOfDepartmentTemplate").html()),

    selectors: {
        createDepartment: "#addDepartment",
        changeDepartment: "#changeDepartment",
        departmentTitle: "#departmentName",
        headOfDepartment: "#headOfDepartment",
        specialization: "#departmentSpecialization"
    },

    constants: {
        ENTER_KEY_CODE: 13
    },

    initialize: function(options) {
        this.collection = options.collection;
        this.faculty = options.faculty;
        this.teachersCollection = options.teachersCollection;
        this.collection.on("add", $.proxy(this._renderDepartment, this));
        this.publisher.on('change:department', $.proxy(this._onDepartmentChange, this));
        this.collection.reset().fetch();
    },

    _attachEvents: function() {
        this.$(this.selectors.createDepartment).on('click', $.proxy(this._addDepartment, this));
        this.$(this.selectors.changeDepartment).on('click', $.proxy(this._changeDepartment, this));
        this.$(this.selectors.departmentTitle).on('keypress', $.proxy(this._onEnter, this))

    },

    _onDepartmentChange: function(model) {
        $(this.selectors.departmentTitle).val(model.getTitle());
        $(this.selectors.specialization).val(model.getSpecialization());
        $(this.selectors.headOfDepartment).val(_.isObject(model.getHeadOfDepartment()) ? model.getHeadOfDepartment().id : model.getHeadOfDepartment());
        this.$(this.selectors.changeDepartment).data('model', model);
        this.$(this.selectors.createDepartment).addClass('no-display');
        this.$(this.selectors.changeDepartment).removeClass('no-display');
        this.$(this.selectors.headOfDepartment).removeClass('no-display');
    },

    _onEnter: function(e) {
        if(e.keyCode === this.constants.ENTER_KEY_CODE) {
            this._addDepartment();
        }
    },

    _addDepartment: function() {
        var departmentModel = new DepartmentModel({
            faculty: this.faculty
        });
        departmentModel.setTitle(this.$(this.selectors.departmentTitle).val());
        departmentModel.setSpecialization(this.$(this.selectors.specialization).val());
        this.$(this.selectors.departmentTitle).val("");
        this.$(this.selectors.specialization).val("");
        departmentModel.save({}, {success: $.proxy(function() {
                    this.collection.add(departmentModel);
                }, this)});
        return false;
    },

    _changeDepartment: function() {
        var departmentModel = this.$(this.selectors.changeDepartment).data('model'),
            headOfDepartment = this.$(this.selectors.headOfDepartment).val();
        if(headOfDepartment) {
            departmentModel.setHeadOfDepartment(+headOfDepartment);
        } else {
            departmentModel.setHeadOfDepartment(null);
        }
        departmentModel.setTitle(this.$(this.selectors.departmentTitle).val());
         departmentModel.setSpecialization(this.$(this.selectors.specialization).val());
        departmentModel.save();
        this.$(this.selectors.departmentTitle).val("");
        this.$(this.selectors.specialization).val("");
        this.$(this.selectors.headOfDepartment).addClass('no-display');
        this.$(this.selectors.changeDepartment).addClass('no-display');
        this.$(this.selectors.createDepartment).removeClass('no-display');
    },

    _renderDepartment: function(model) {
        this.$("#departments").append(
            new DepartmentView({
            model: model
        }).render().el
        );
    },

     _fillHeadOfDepartmentList: function() {
        this.teachersCollection.reset().fetch({
            success: $.proxy(function () {
                this.teachersCollection.each(function(model) {
                    this.$('#headOfDepartment').append(this.optionHeadOfDepartmentTemplate(model.toJSON()));
                }, this);
            }, this)
        });
    },

    render: function() {
        this.$el.html(this.template(this.faculty.toJSON));
        this._attachEvents();
        this._fillHeadOfDepartmentList();
        return this;
    }


});