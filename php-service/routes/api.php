<?php

use Illuminate\Support\Facades\Route;

Route::get('/health', function () {
    return response()->json([
        'app' => 'php-validation-service',
        'version' => '1.0.0',
        'status' => 'healthy',
        'environment' => app()->environment(),
        'timestamp' => now()->toISOString(),
    ]);
});
