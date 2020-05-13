pipeline {
  agent {
    label "jenkins-python"
  }
  environment {
    ORG = 'mmontalvo'
    APP_NAME = 'rest-django-payments'
    CHARTMUSEUM_CREDS = credentials('jenkins-x-chartmuseum')
    DOCKER_REGISTRY_ORG = 'mmontalvo'
  }
  stages {
    stage('build branch') {
      when {
        branch 'PR-*'
      }
      environment {
        PREVIEW_VERSION = "0.0.0-SNAPSHOT-$BRANCH_NAME-$BUILD_NUMBER"
        PREVIEW_NAMESPACE = "$APP_NAME-$BRANCH_NAME".toLowerCase()
        HELM_RELEASE = "$PREVIEW_NAMESPACE".toLowerCase()
      }
      steps {
        container('python') {
          sh "docker build --network host -t $DOCKER_REGISTRY/$ORG/$APP_NAME:$PREVIEW_VERSION ."
          sh "docker push $DOCKER_REGISTRY/$ORG/$APP_NAME:$PREVIEW_VERSION"

          dir('./charts/preview') {
            sh "make preview"
            sh "jx preview --app $APP_NAME --dir ../.."
            sh "kubectl create namespace $PREVIEW_NAMESPACE --dry-run -o yaml | kubectl apply -f -"
            sh "jx preview --app $APP_NAME --dir ../.. --timeout=15m"
          }
          // sh "python -m unittest"
          // sh "export VERSION=$PREVIEW_VERSION && skaffold build -f skaffold.yaml"
          // sh "jx step post build --image $DOCKER_REGISTRY/$ORG/$APP_NAME:$PREVIEW_VERSION"
          // dir('./charts/preview') {
          //   sh "make preview"
          //   sh "kubectl create namespace $PREVIEW_NAMESPACE --dry-run -o yaml | kubectl apply -f -"
          //   sh "jx preview --app $APP_NAME --dir ../.. --timeout=15m"
          // }
        }
      }
    }
    stage('Build Release') {
      when {
        branch 'master'
      }
      steps {
        container('python') {
          sh "git checkout master"
          sh "git config --global credential.helper store"
          sh "jx step git credentials"

          sh "jx step next-version --use-git-tag-only --tag"
          sh "docker build  --network host -t $DOCKER_REGISTRY/$ORG/$APP_NAME:\$(cat VERSION) ."
          sh "docker push $DOCKER_REGISTRY/$ORG/$APP_NAME:\$(cat VERSION)"

          dir('./charts/pricing') {
            sh "jx step helm release"
          }

          // so we can retrieve the version in later steps
          // sh "echo \$(jx-release-version) > VERSION"
          // sh "jx step tag --version \$(cat VERSION)"
          // sh "python -m unittest"
          // sh "export VERSION=`cat VERSION` && skaffold build -f skaffold.yaml"
          // sh "jx step post build --image $DOCKER_REGISTRY/$ORG/$APP_NAME:\$(cat VERSION)"
        }
      }
    }
    stage('Promote to Environments') {
      when {
        branch 'master'
      }
      steps {
        container('python') {
          dir('./charts/rest-django-payments') {
            sh "jx step changelog --version v\$(cat ../../VERSION)"

            // release the helm chart
            sh "jx step helm release"

            // promote through all 'Auto' promotion Environments
            sh "jx promote -b --all-auto --timeout 1h --version \$(cat ../../VERSION)"
          }
        }
      }
    }
  }
  post {
        always {
          cleanWs()
        }
  }
}
