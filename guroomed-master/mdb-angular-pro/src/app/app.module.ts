import { ToastModule } from './typescripts/pro/alerts/toast/toast.module';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';

import { MDBBootstrapModule } from './typescripts/free';
import { MDBBootstrapModulePro } from './typescripts/pro/index';

import { AgmCoreModule } from '@agm/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app.routing';
import { AdminModule } from './admin/admin.module';
import { HomeModule } from 'app/home/home.module';
import { MycoursesModule } from 'app/mycourses/mycourses.module';
import { BecomeInstructorModule } from './become-instructor/become-instructor.module';
import { CourseManagementModule } from './course-management/course-management.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { MDBSpinningPreloader } from './typescripts/pro/index';

import { AuthenticationService } from 'app/services/authentication.service';
import { ElasticService } from 'app/shared/elastic-search/elastic.service';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { CourseDetailService } from 'app/services/coursedetail/course-detail.service';
import { ShoppingcartService } from 'app/services/shopcart/shoppingcart.service';
import { StorageService } from 'app/services/localstore/storage.service';
import { LoaderService } from 'app/shared/loader/loader.service';
import { CheckoutService } from './cart/checkout.service';
import { TransactionService } from './transaction/transaction.service';
import { ProfileService } from './profile/profile.service';

import { NavbarComponent } from './shared/navbar/navbar.component';
import { ErrorComponent } from './error/error.component';
import { FooterComponent } from './shared/footer/footer.component';
import { LoginComponent } from './login/login.component';
import { ElasticSearchComponent } from './shared/elastic-search/elastic-search.component';
import { CourseSearchComponent } from './course-search/course-search.component';
import { CourseFliterComponent } from './course-fliter/course-fliter.component';
import { CourseFilterService } from 'app/course-fliter/course-filter.service';
import { SignUpComponent } from './sign-up/sign-up.component';
import { CourseDetailComponent } from './course-detail/course-detail.component';
import { CartComponent } from './cart/cart.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { SuccessMessageComponent } from './forgot-password/success-message/success-message.component';
import { DeleteAccountComponent } from './profile/delete-account/delete-account.component';
import { ImageUploadComponent } from './profile/image-upload/image-upload.component';
import { ResetPasswordComponent } from './forgot-password/reset-password/reset-password.component';
import { CourseOverviewComponent } from './course-overview/course-overview.component';
import { OverviewComponent } from './course-overview/overview/overview.component';
import { ContentComponent } from './course-overview/content/content.component';
import { QuestionsComponent } from './course-overview/questions/questions.component';
import { BookmarksComponent } from './course-overview/bookmarks/bookmarks.component';
import { AnnouncementsComponent } from './course-overview/announcements/announcements.component';
import { TokenInterceptorService } from './shared/token-interceptor.service';
import { TermsComponent } from './terms and policy/terms/terms.component';

import { StarRatingModule } from 'angular-star-rating';
import { FeedbackComponent } from './shared/feedback/feedback.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ErrorComponent,
    FooterComponent,
    LoginComponent,
    ElasticSearchComponent,
    CourseSearchComponent,
    CourseFliterComponent,
    SignUpComponent,
    CourseDetailComponent,
    CartComponent,
    ForgotPasswordComponent,
    SuccessMessageComponent,
    DeleteAccountComponent,
    ImageUploadComponent,
    ResetPasswordComponent,
    CourseOverviewComponent,
    OverviewComponent,
    ContentComponent,
    QuestionsComponent,
    BookmarksComponent,
    AnnouncementsComponent,
    TermsComponent,
    FeedbackComponent,
  ],
  imports: [
    BrowserModule,
    AdminModule,
    HomeModule,
    MycoursesModule,
    BecomeInstructorModule,
    CourseManagementModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    ToastModule.forRoot(),
    MDBBootstrapModule.forRoot(),
    MDBBootstrapModulePro.forRoot(),
    NgbModule.forRoot(),
    StarRatingModule.forRoot(),
    AgmCoreModule.forRoot({
      // https://developers.google.com/maps/documentation/javascript/get-api-key?hl=en#key
      apiKey: 'Your_api_key'
    })
  ],
  providers: [
    MDBSpinningPreloader,
    AuthenticationService,
    ElasticService,
    CourseFilterService,
    NavbarService,
    CourseDetailService,
    ShoppingcartService,
    StorageService,
    LoaderService,
    CheckoutService,
    TransactionService,
    ProfileService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptorService,
      multi: true
    }
  ],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }
