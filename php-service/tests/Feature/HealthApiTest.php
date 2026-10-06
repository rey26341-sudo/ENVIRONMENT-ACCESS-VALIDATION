<?php

namespace Tests\Feature;

use Tests\TestCase;

class HealthApiTest extends TestCase
{
    public function test_health_endpoint_returns_healthy_status(): void
    {
        $response = $this->getJson('/api/health');

        $response
            ->assertStatus(200)
            ->assertJson([
                'app' => 'php-validation-service',
                'version' => '1.0.0',
                'status' => 'healthy',
            ]);
    }
}
