import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NewCourseListComponent } from './course-manager/new-course-list/new-course-list.component';
import { ManagementDashboardComponent } from './management-dashboard/management-dashboard.component';
import { CreateReviewerComponent } from './course-manager/create-reviewer/create-reviewer.component';
import { CourseReviewerComponent } from './course-reviewer/course-reviewer.component';
import { ManagerGuard } from '../admin/manager.guard';
import { ReviewerGuard } from '../admin/reviewer.guard';
import { ReviewerListComponent } from './course-manager/reviewer-list/reviewer-list.component';

const routes: Routes = [
  {
    path: 'course-management/dashboard',
    component: ManagementDashboardComponent,
    canActivate: [ManagerGuard],
    children: [
      { path: 'all', component: NewCourseListComponent },
    ]
  },
  {
    path: 'course-management',
    component: ManagementDashboardComponent,
    canActivate: [ManagerGuard],
    children: [
      { path: 'create-reviewer', component: CreateReviewerComponent },
      { path: 'reviewer-list', component: ReviewerListComponent}
    ]
  },
  {
    path: 'course-reviewer/dashboard',
    component: ManagementDashboardComponent,
    canActivate: [ReviewerGuard],
    children: [
      { path: 'all', component: CourseReviewerComponent }
    ]
  }

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CourseManagementRouting { }
