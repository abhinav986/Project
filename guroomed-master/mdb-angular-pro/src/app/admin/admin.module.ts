import { NgModule, ModuleWithProviders } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { AdminComponent } from './admin.component';
import { HomeDataService } from 'app/home/home-data.service';
import { AuthGuardService } from 'app/admin/services/auth-guard.service';
import { ProfileComponent } from 'app/profile/profile.component';
import { TransactionComponent } from 'app/transaction/transaction.component';
import { CheckoutComponent } from '../checkout/checkout.component';
import { EditProfileComponent } from '../profile/edit-profile/edit-profile.component';
import { MDBBootstrapModulePro } from '../typescripts/pro';
import { ChangePasswordComponent } from '../profile/change-password/change-password.component';
import { ToastModule } from 'app/typescripts/pro/alerts';
import { DeleteAccountComponent } from '../profile/delete-account/delete-account.component';
import { ImageUploadComponent } from '../profile/image-upload/image-upload.component';
import { CartComponent } from '../cart/cart.component';
import { OrderSuccessComponent } from '../order-success/order-success.component';

const adminRoutes: Routes = [
	{
		path: 'admin',
		canActivate: [AuthGuardService],
		redirectTo: '',
		pathMatch: 'full'
	},
	{
		path: 'profile',
		canActivate: [AuthGuardService],
		component: ProfileComponent,
		children: [
			{
				path: 'editProfile',
				component: EditProfileComponent,
				outlet: 'profile'
			},
			{
				path: 'changePassword',
				component: ChangePasswordComponent,
				outlet: 'profile'
			},
			{
				path: 'deleteAccount',
				component: DeleteAccountComponent,
				outlet: 'profile'
			},
			{
				path: 'uploadImage',
				component: ImageUploadComponent,
				outlet: 'profile'
			}
		]
	},
	{
		path: 'transaction',
		canActivate: [AuthGuardService],
		component: TransactionComponent
	},
	{
		path: 'checkout',
		canActivate: [AuthGuardService],
		component: CheckoutComponent
	},
	{
		path: 'cart/items',
		canActivate: [AuthGuardService],
		component: CartComponent
	},
	{
		path: 'orderSuccess',
		canActivate: [AuthGuardService],
		component: OrderSuccessComponent
	}
];

@NgModule({
	imports: [
		CommonModule,
		FormsModule,
		ToastModule.forRoot(),
		RouterModule.forChild(adminRoutes),
		MDBBootstrapModulePro.forRoot()
	],
	exports: [
		RouterModule
	],
	declarations: [
		AdminComponent,
		ProfileComponent,
		TransactionComponent,
		CheckoutComponent,
		EditProfileComponent,
		ChangePasswordComponent,
		OrderSuccessComponent
	],
	providers: [
		HomeDataService,
		AuthGuardService
	]
})
export class AdminModule {
	static forRoot(): ModuleWithProviders {
		return {
			ngModule: AdminModule,
			providers: [HomeDataService]
		};
	}
}