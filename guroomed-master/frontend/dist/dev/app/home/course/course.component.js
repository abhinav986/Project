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
var CourseComponent = (function () {
    function CourseComponent() {
    }
    Object.defineProperty(CourseComponent.prototype, "data", {
        get: function () { return this._data; },
        set: function (data) {
            this._data = (data) || { name: "peace" };
        },
        enumerable: true,
        configurable: true
    });
    CourseComponent.prototype.ngOnInit = function () { };
    __decorate([
        core_1.Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], CourseComponent.prototype, "data", null);
    CourseComponent = __decorate([
        core_1.Component({
            selector: 'app-course',
            templateUrl: '../app/home/course/course.component.html',
            styleUrls: ['../app/home/course/course.component.css']
        }),
        __metadata("design:paramtypes", [])
    ], CourseComponent);
    return CourseComponent;
}());
exports.CourseComponent = CourseComponent;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2NvdXJzZS9jb3Vyc2UuY29tcG9uZW50LnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7O0FBQUEsc0NBQXdFO0FBUXhFO0lBT0U7SUFBZSxDQUFDO0lBSmhCLHNCQUFJLGlDQUFJO2FBR1IsY0FBa0IsTUFBTSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO2FBSHRDLFVBQVMsSUFBUTtZQUNmLElBQUksQ0FBQyxLQUFLLEdBQUcsQ0FBQyxJQUFJLENBQUMsSUFBSSxFQUFDLElBQUksRUFBQyxPQUFPLEVBQUMsQ0FBQztRQUN4QyxDQUFDOzs7T0FBQTtJQUtELGtDQUFRLEdBQVIsY0FBWSxDQUFDO0lBUGI7UUFERyxZQUFLLEVBQUU7OzsrQ0FHVDtJQUxVLGVBQWU7UUFMM0IsZ0JBQVMsQ0FBQztZQUNULFFBQVEsRUFBRSxZQUFZO1lBQ3RCLFdBQVcsRUFBRSwwQ0FBMEM7WUFDdkQsU0FBUyxFQUFFLENBQUMseUNBQXlDLENBQUM7U0FDdkQsQ0FBQzs7T0FDVyxlQUFlLENBWTNCO0lBQUQsc0JBQUM7Q0FaRCxBQVlDLElBQUE7QUFaWSwwQ0FBZSIsImZpbGUiOiJhcHAvaG9tZS9jb3Vyc2UvY291cnNlLmNvbXBvbmVudC5qcyIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IENvbXBvbmVudCwgT25Jbml0LCBJbnB1dCwgU2ltcGxlQ2hhbmdlcyB9IGZyb20gJ0Bhbmd1bGFyL2NvcmUnO1xyXG5pbXBvcnQge0NvdXJzZX0gZnJvbSAnLi9jb3Vyc2UnO1xyXG5cclxuQENvbXBvbmVudCh7XHJcbiAgc2VsZWN0b3I6ICdhcHAtY291cnNlJyxcclxuICB0ZW1wbGF0ZVVybDogJy4uL2FwcC9ob21lL2NvdXJzZS9jb3Vyc2UuY29tcG9uZW50Lmh0bWwnLFxyXG4gIHN0eWxlVXJsczogWycuLi9hcHAvaG9tZS9jb3Vyc2UvY291cnNlLmNvbXBvbmVudC5jc3MnXVxyXG59KVxyXG5leHBvcnQgY2xhc3MgQ291cnNlQ29tcG9uZW50IGltcGxlbWVudHMgT25Jbml0IHtcclxuICAgIF9kYXRhOmFueTtcclxuICAgIEBJbnB1dCgpXHJcbiAgc2V0IGRhdGEoZGF0YTphbnkpIHtcclxuICAgIHRoaXMuX2RhdGEgPSAoZGF0YSkgfHwge25hbWU6XCJwZWFjZVwifTtcclxuICB9XHJcbiAgZ2V0IGRhdGEoKTogYW55IHsgcmV0dXJuIHRoaXMuX2RhdGE7IH1cclxuICBjb25zdHJ1Y3RvcigpIHt9XHJcblxyXG5cclxuICBuZ09uSW5pdCgpIHt9XHJcblxyXG59XHJcbiJdfQ==
