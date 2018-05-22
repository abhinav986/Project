import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Routes } from '@angular/router/src/config';
import { HomeComponent } from './home/home.component';
import { ErrorComponent } from './error/error.component';
import { CourseFliterComponent } from 'app/course-fliter/course-fliter.component';
import { CourseDetailComponent } from 'app/course-detail/course-detail.component';
import { CartComponent } from 'app/cart/cart.component';
import { SuccessMessageComponent } from './forgot-password/success-message/success-message.component';
import { ResetPasswordComponent } from './forgot-password/reset-password/reset-password.component';
import { CourseOverviewComponent } from './course-overview/course-overview.component';
import { OverviewComponent } from './course-overview/overview/overview.component';
import { ContentComponent } from './course-overview/content/content.component';
import { QuestionsComponent } from './course-overview/questions/questions.component';
import { BookmarksComponent } from './course-overview/bookmarks/bookmarks.component';
import { AnnouncementsComponent } from './course-overview/announcements/announcements.component';
import { TermsComponent } from './terms and policy/terms/terms.component';
import { FeedbackComponent } from './shared/feedback/feedback.component';
// import { CreatequizComponent } from './quiz/createquiz/createquiz.component';
// import { CreatequestionComponent } from './quiz/createquestion/createquestion.component';
// import { ViewquizComponent } from './quiz/viewquiz/viewquiz.component';

const appRoutes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'courses/:searchStr',
    component: CourseFliterComponent
  },
  {
    path: 'coursedetails/:id',
    component: CourseDetailComponent
  },
  {
    path: 'course/feedback',
    component: FeedbackComponent
  },
  {
    path: 'cart',
    component: CartComponent
  },
  {
    path: 'forgotSuccessMsg',
    component: SuccessMessageComponent
  },
  {
    path: 'resetpassword',
    component: ResetPasswordComponent
  },
  {
    path: 'course-overview',
    component: CourseOverviewComponent,
    children: [
      { path: 'overview', component: OverviewComponent},
      { path: 'content', component: ContentComponent},
      { path: 'questions', component: QuestionsComponent},
      { path: 'bookmarks', component: BookmarksComponent},
      { path: 'announcements', component: AnnouncementsComponent }
    ]
  },
  {
    path: 'terms-and-policy',
    component: TermsComponent
  },
  {
    path: '**',
    component: ErrorComponent
  }
]

@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes,
      {useHash: true}
    )
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }

