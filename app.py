from flask import Flask, jsonify
import time
from kubernetes import client, config

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Automate all the things!",
        "timestamp": 1529729125  # Hardcoded timestamp for demonstration
    })

if __name__ == '__main__':
    # Load Kubernetes configuration from default location or from environment variables
    config.load_kube_config()

    # Create Kubernetes API client
    api = client.CoreV1Api()

    # Define deployment YAML
    deployment = client.V1Deployment()
    deployment.metadata = client.V1ObjectMeta(name="xyz-app")
    deployment.spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(match_labels={"app": "xyz-app"}),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "xyz-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="xyz-app",
                        image="your-docker-image",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )

    # Create deployment
    api.create_namespaced_deployment(body=deployment, namespace="default")

    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
