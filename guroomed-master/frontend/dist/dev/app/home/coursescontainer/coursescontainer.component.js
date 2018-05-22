"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var CoursescontainerComponent = (function () {
    function CoursescontainerComponent() {
    }
    Object.defineProperty(CoursescontainerComponent.prototype, "courses", {
        get: function () { return this._courses; },
        set: function (courses) {
            this._courses = (courses) || [];
        },
        enumerable: true,
        configurable: true
    });
    CoursescontainerComponent.prototype.ngOnChanges = function (changes) {
    };
    CoursescontainerComponent.prototype.ngOnInit = function () { };
    __decorate([
        core_1.Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], CoursescontainerComponent.prototype, "courses", null);
    CoursescontainerComponent = __decorate([
        core_1.Component({
            selector: 'app-coursescontainer',
            templateUrl: '../app/home/coursescontainer/coursescontainer.component.html',
            styleUrls: ['../app/home/coursescontainer/coursescontainer.component.css']
        }),
        __metadata("design:paramtypes", [])
    ], CoursescontainerComponent);
    return CoursescontainerComponent;
}());
exports.CoursescontainerComponent = CoursescontainerComponent;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2NvdXJzZXNjb250YWluZXIvY291cnNlc2NvbnRhaW5lci5jb21wb25lbnQudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7QUFBQSxzQ0FBd0U7QUFTeEU7SUFZRTtJQUFnQixDQUFDO0lBUmpCLHNCQUFJLDhDQUFPO2FBR1gsY0FBcUIsTUFBTSxDQUFDLElBQUksQ0FBQyxRQUFRLENBQUMsQ0FBQyxDQUFDO2FBSDVDLFVBQVksT0FBVztZQUNyQixJQUFJLENBQUMsUUFBUSxHQUFHLENBQUMsT0FBTyxDQUFDLElBQUksRUFBRSxDQUFDO1FBQ2xDLENBQUM7OztPQUFBO0lBR0EsK0NBQVcsR0FBWCxVQUFZLE9BQXNCO0lBQ2xDLENBQUM7SUFJRiw0Q0FBUSxHQUFSLGNBQWEsQ0FBQztJQVZkO1FBREMsWUFBSyxFQUFFOzs7NERBR1A7SUFOVSx5QkFBeUI7UUFMckMsZ0JBQVMsQ0FBQztZQUNULFFBQVEsRUFBRSxzQkFBc0I7WUFDaEMsV0FBVyxFQUFFLDhEQUE4RDtZQUMzRSxTQUFTLEVBQUUsQ0FBQyw2REFBNkQsQ0FBQztTQUMzRSxDQUFDOztPQUNXLHlCQUF5QixDQWdCckM7SUFBRCxnQ0FBQztDQWhCRCxBQWdCQyxJQUFBO0FBaEJZLDhEQUF5QiIsImZpbGUiOiJhcHAvaG9tZS9jb3Vyc2VzY29udGFpbmVyL2NvdXJzZXNjb250YWluZXIuY29tcG9uZW50LmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgQ29tcG9uZW50LCBPbkluaXQsIFNpbXBsZUNoYW5nZXMsIElucHV0IH0gZnJvbSAnQGFuZ3VsYXIvY29yZSc7XHJcbmltcG9ydCB7Q291cnNlfSBmcm9tICcuLi9jb3Vyc2UvY291cnNlJztcclxuaW1wb3J0IHtDb3Vyc2VDb21wb25lbnR9IGZyb20gJy4uL2NvdXJzZS9jb3Vyc2UuY29tcG9uZW50JztcclxuXHJcbkBDb21wb25lbnQoe1xyXG4gIHNlbGVjdG9yOiAnYXBwLWNvdXJzZXNjb250YWluZXInLFxyXG4gIHRlbXBsYXRlVXJsOiAnLi4vYXBwL2hvbWUvY291cnNlc2NvbnRhaW5lci9jb3Vyc2VzY29udGFpbmVyLmNvbXBvbmVudC5odG1sJyxcclxuICBzdHlsZVVybHM6IFsnLi4vYXBwL2hvbWUvY291cnNlc2NvbnRhaW5lci9jb3Vyc2VzY29udGFpbmVyLmNvbXBvbmVudC5jc3MnXVxyXG59KVxyXG5leHBvcnQgY2xhc3MgQ291cnNlc2NvbnRhaW5lckNvbXBvbmVudCBpbXBsZW1lbnRzIE9uSW5pdCB7XHJcbiAgX2NvdXJzZXM6YW55O1xyXG5cclxuICBASW5wdXQoKVxyXG4gIHNldCBjb3Vyc2VzKGNvdXJzZXM6YW55KSB7XHJcbiAgICB0aGlzLl9jb3Vyc2VzID0gKGNvdXJzZXMpIHx8IFtdO1xyXG4gIH1cclxuICBnZXQgY291cnNlcygpOiBhbnkgeyByZXR1cm4gdGhpcy5fY291cnNlczsgfVxyXG5cclxuICAgbmdPbkNoYW5nZXMoY2hhbmdlczogU2ltcGxlQ2hhbmdlcyl7XHJcbiAgIH1cclxuXHJcbiAgY29uc3RydWN0b3IoKSB7IH1cclxuXHJcbiAgbmdPbkluaXQoKSB7IH1cclxuXHJcbn1cclxuIl19
